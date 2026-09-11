# 005 · Text Chunking Processor

**Status:** implemented ✅

## What it does

Automatically splits long Russian textbook passages (exceeding recommended length thresholds, e.g., 1000–2000 characters) into natural, smaller text chunks based on sentence boundaries, punctuation, and paragraphs without cutting words in half.

## Why

Sending very large blocks of text to the speech engine can cause timeouts, network lag, or audio generation failures. Chunking ensures reliable audio generation for long textbook exercises while preserving natural phonetic pauses between sentences.

## Acceptance criteria

- [x] Chunking utility function splits long text strings into an ordered list of smaller text chunks based on sentence punctuation (`.`, `!`, `?`, `\n`).
- [x] Each chunk strictly stays under a configurable max character limit (e.g., 1000 characters).
- [x] Preserves full words and sentence boundaries (never splits a word in the middle).
- [x] Recombines small fragments cleanly so no orphaned punctuation remains.
- [x] Comprehensive unit test suite verifies correct splitting across multi-paragraph textbook excerpts.

## Out of scope

- Multi-file batch background processing or persistent queue databases (Celery/Redis).
- Automatic audio stitching on the server side (frontend handles sequential playback if needed).