# Byte Pair Encoding (BPE) Class

This repository contains a Python implementation of the Byte Pair Encoding (BPE) algorithm taking inspiration from Karpathy's tutorial :) and GPT-2 tokenization algorithm. BPE is a subword tokenization technique widely used in modern Natural Language Processing (NLP) pipelines, particularly for training large language models (LLMs). This implementation provides methods for training the BPE model, encoding a UTF-8 string into a list of tokens, and decoding tokens back into a string.

## Overview

The `BPE` class is designed to:
- **Train on text data:** Learn merge operations by iteratively combining the most frequent adjacent tokens.
- **Encode:** Convert a UTF-8 string into a compact sequence of tokens.
- **Decode:** Reconstruct the original string from the tokenized representation.
- **Provide Compression Statistics:** Display the reduction in size achieved through token merging.

The algorithm works by first converting input text into its UTF-8 byte representation (integers from 0 to 255) and then iteratively merging the most frequent pairs of tokens until the vocabulary size reaches the specified limit.

## Class Structure and Methods

### `__init__(self, vocab_size)`
- **Purpose:** Initialize the BPE model with a target vocabulary size.
- **Parameters:**
  - `vocab_size` (int): The desired size of the vocabulary.
- **Attributes:**
  - `self.merges`: A dictionary to store merge operations (i.e., mapping new tokens to their constituent tokens).

### `get_pairs(self, data)`
- **Purpose:** Count the frequency of each pair of consecutive tokens in the input data.
- **Parameters:**
  - `data` (list of int): A list of tokens (integers).
- **Returns:** A dictionary with pairs as keys and their frequency as values.

### `merge(self, pairs, most_frequent_pair, idx)`
- **Purpose:** Merge all occurrences of the most frequent pair in the token sequence into a new token.
- **Parameters:**
  - `pairs` (list of int): The current list of tokens.
  - `most_frequent_pair` (tuple): The most frequent token pair and its frequency.
  - `idx` (int): The new token index to assign to the merged pair.
- **Returns:** A new list of tokens with the most frequent pair merged.

### `train(self, data)`
- **Purpose:** Train the BPE model on a given text.
- **Process:**
  1. Convert text to a UTF-8 byte sequence.
  2. Map each byte to an integer (0–255).
  3. Iteratively merge the most frequent pairs until reaching the desired vocabulary size.
  4. Print statistics (initial bits, final bits, compression ratio).

### `encode(self, data)`
- **Purpose:** Encode a UTF-8 string into a list of tokens.
- **Process:** Convert the string into bytes and then integers. Replace sequences based on the learned merges.
- **Returns:** A list of integers representing the tokenized data.

### `decode_token(self, token)`
- **Purpose:** Recursively decode a single token into its original byte sequence.
- **Process:** If the token is less than 256, it represents a single byte. Otherwise, it is a merged token whose components are recursively decoded.
- **Returns:** A byte string representing the decoded token.

### `decode(self, data)`
- **Purpose:** Decode a list of tokens back into a UTF-8 string.
- **Process:** Use `decode_token` on each token, join the resulting byte sequences, and convert them to a string.
- **Returns:** The reconstructed UTF-8 string.

## Usage Example

Below is an example of how to use the BPE class:

```python
if __name__ == "__main__":
    # Initialize the BPE model with a desired vocabulary size (e.g., 260)
    bpe = BPE(vocab_size=260)
    
    # Example text to train on
    sample_text = "This is a sample text to demonstrate the BPE algorithm. It compresses data by merging frequent token pairs."
    
    # Train the BPE model on the sample text
    bpe.train(sample_text)
    
    # Encode the text into tokens
    tokens = bpe.encode(sample_text)
    print("Encoded Tokens:", tokens)
    
    # Decode the tokens back into a string
    decoded_text = bpe.decode(tokens)
    print("Decoded Text:", decoded_text)
