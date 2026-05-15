# MiniMax Model Issue Analysis

## Summary

**Problem:** The MiniMaxAI/MiniMax-M2.5 model returns empty content when processing extraction requests, despite HTTP 200 responses.

**Root Cause:** Likely rate limiting or quota exceeded on the LLM endpoint (`https://llm.scads.ai/v1`)

## Evidence

### 1. Ping Test Results
```
Testing model: MiniMaxAI/MiniMax-M2.5
Endpoint: https://llm.scads.ai/v1
API Key: ✓
Timeout: 120s

Sending simple test prompt...
✅ SUCCESS
   Response: ''                          ← EMPTY CONTENT
   Prompt tokens: 29
   Completion tokens: 10                ← BUT API RETURNED TOKENS
```

**Conclusion:** The model accepts requests and processes them (API reports tokens), but returns empty content. This is a classic rate-limit behavior where the API returns HTTP 200 instead of HTTP 429.

### 2. Extraction Attempt Results
```
WARNING: Model 'MiniMaxAI/MiniMax-M2.5' returned empty content 
         (input_chars=15962, duration=20.76 s) — likely rate limit or quota issue
```

The script retried 3 times (exponential backoff: 5s, 20s, 60s) but all attempts returned empty content:
- Attempt 1: 20.76s → empty
- Attempt 2: 21.09s → empty  
- Attempt 3: 18.61s → empty

## Diagnosis

The empty content with HTTP 200 response indicates one of:

1. **Rate Limiting** - The endpoint is rejecting requests but returning 200 with empty body instead of 429
2. **Quota Exceeded** - The account/key has hit usage limits
3. **Model Overload** - The service is too busy to process requests
4. **Endpoint Configuration Issue** - Misconfigured proxy or reverse proxy returning 200 for errors

## Enhanced Error Reporting

The compare_models.py script now includes:

✅ **Specific error classification:**
```
- RATE_LIMIT_ERROR (HTTP 429)
- AUTH_ERROR (HTTP 401/403)  
- SERVER_ERROR (HTTP 500+)
- API_ERROR (other HTTP codes)
- CONNECTION_ERROR
- Empty content explicitly flagged as "likely rate limit or quota issue"
```

✅ **Better diagnostics in logs:**
- Error type and HTTP status code
- Detailed error messages from API
- Clear indication when retrying due to transient errors

✅ **Ping test script** (`scripts/test_model_ping.py`):
```bash
# Test a model with simple request
uv run scripts/test_model_ping.py MiniMaxAI/MiniMax-M2.5
```

## Recommendations

1. **For immediate use:**
   - Use the GLM 4.7 model (qwen3.6-35b-a3b in production)
   - Try a different model if available
   - Wait and retry later if quota is exceeded

2. **For endpoint administrators:**
   - Configure the endpoint to return HTTP 429 instead of 200 for rate limits
   - Add rate-limit response headers (`Retry-After`, `X-RateLimit-*`)
   - Check endpoint logs for quota/usage information

3. **For future comparisons:**
   - Run model comparisons during off-peak hours
   - Monitor `experiments/logs/` files for detailed error logs
   - Use the test script first to verify model availability before large runs

## Files Modified

- `scripts/compare_models.py` - Enhanced error handling with specific exception types
- `backend/llm_extractor.py` - Better logging for empty content and API errors
- `scripts/test_model_ping.py` - New diagnostic test script
