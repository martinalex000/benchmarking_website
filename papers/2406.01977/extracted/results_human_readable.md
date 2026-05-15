# Extraction: arXiv:2406.01977
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: LOW

## Proposed Model: GT with PE
- Type: GraphTransformer

## Baseline Models Identified

- **GT without PE** (from: this paper)
- **GCN** (from: KW17)
- **GT (without PE)** (from: this paper)

## Extraction Notes

[Cora] The provided text contains only tables with notations, dataset statistics, and fractions of
discriminative nodes. It does not contain any experimental result tables reporting Accuracy or other
performance metrics for the Cora dataset or any other dataset. Therefore, no quantitative results
could be extracted. [PubMed] The paper discusses results for PubMed in Figures 1 and 2 (referenced
as figure: b_z and figure: compare) and mentions state-of-the-art comparisons in the text (e.g.,
'Our PubMed and Actor test accuracy is close to the state-of-art...'). However, the actual numerical
values for the proposed model (GT with PE), the baselines (GT without PE, GCN), and the specific
SOTA comparisons are contained within the images of these figures, not in the provided text or
tables. The provided tables only contain dataset statistics and internal analysis metrics (fraction
of discriminative nodes), not the final benchmark accuracy scores. Therefore, no quantitative
results could be extracted. [Actor] failed: 3 validation errors for ExtractionOutput results.0.value
Input should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For
further information visit https://errors.pydantic.dev/2.13/v/float_type results.1.value   Input
should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For further
information visit https://errors.pydantic.dev/2.13/v/float_type results.2.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type [PascalVOC-SP-1G] The paper mentions PascalVOC-
SP-1G and references Figures 1 and 2 for test accuracy results on this dataset. However, the
provided text only contains the captions and descriptions of these figures, not the actual data
values (numerical accuracy scores) contained within the figures. The tables provided in the text
contain dataset statistics and theoretical fractions (e.g., fraction of discriminative nodes), but
no experimental performance metrics (Accuracy) for any model on PascalVOC-SP-1G. Therefore, no
quantitative results could be extracted.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*