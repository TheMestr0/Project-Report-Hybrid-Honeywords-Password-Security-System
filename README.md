# Project #1: Honeywords Password Algorithm

A Python implementation of honeywords password security system combining multiple techniques.

## Overview

This project implements a complete honeywords system with three components:

1. **Chaffing Algorithm** - Character-based honeyword generation
2. **Real-Decoys Generator** - Realistic pattern-based decoy generation
3. **Merged System** - Combined approach for optimal security

## Components

### 1. HoneywordsAlgorithm (Chaffing Technique)
- Generates honeywords through character substitution, addition, and removal
- Real password hidden at random position in set
- SHA-256 hashing for secure storage
- Password verification with honeyword detection

### 2. RealDecoysGenerator
- Analyzes password patterns (length, case, digits, special chars)
- Generates realistic decoys using:
  - Leetspeak substitutions
  - Common suffixes (numbers, special chars)
  - Case variations
  - Keyboard neighbor patterns
  - Prefix additions

### 3. MergedHoneywordsSystem
- Combines both techniques
- 50% realistic decoys + 50% chaffing-based honeywords
- Provides both believability and cryptographic security

## Usage

```python
from honeywords import HoneywordsAlgorithm, RealDecoysGenerator, MergedHoneywordsSystem

# Chaffing only
pwd = "MySecurePass123!"
algo = HoneywordsAlgorithm(pwd, num_honeywords=19)
honeywords = algo.generate_honeyword_set()
hashed = algo.hash_honeyword_set()

# Real-decoys only
generator = RealDecoysGenerator(pwd, num_decoys=19)
decoys = generator.generate_realistic_decoys()

# Merged system (recommended)
merger = MergedHoneywordsSystem(pwd, total_decoys=19)
merged_set = merger.generate_merged_set()
```

## Running Tests

```bash
python test_runner.py
```

This will execute all three test suites and display:
- Honeyword generation results
- Realistic decoy generation
- Merged system output
- Comprehensive analysis and recommendations

## Test Results

All tests verify:
✓ Honeyword set generation
✓ Real password hidden among decoys
✓ Hash function integrity
✓ Password verification
✓ Pattern analysis accuracy
✓ System integration

## Security Considerations

- **Honeypot Functionality**: Attempted honeyword login indicates breach
- **Password Indistinguishability**: Attackers cannot distinguish real from fake
- **Defense in Depth**: Combines linguistic + cryptographic security
- **Detection Mechanism**: Monitor honeyword attempts for breach alerts

## Recommendations

Use the **Merged System** for production environments where:
- Breach detection is critical
- Defense-in-depth is desired
- User authentication complexity is acceptable

## Files

- `honeywords.py` - Core implementation
- `test_runner.py` - Comprehensive test suite
- `README.md` - This file

## Author

TheMestr0 - Project #1 (2026-03-12)