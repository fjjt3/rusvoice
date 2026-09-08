# Mission

_Defines the purpose of the project. It serves as the reference to decide whether a feature "fits" or not._

## What we are building

A lightweight web application for language learners that converts written textbook excerpts into natural, native-sounding speech in real time. This allows students to practice listening comprehension without needing physical CDs or external audio files.

1. **AI-Powered TTS Engine** — Generates clear native-pronunciation MP3 audio files with adjustable playback speed using Edge-TTS.
2. **FastAPI Backend API** — Exposes high-performance endpoints for real-time audio processing and streaming without saving files to disk.
3. **Student Audio Player Interface** — Provides an intuitive web UI with text input, voice selection, speed controls, and an embedded audio player.

## Target Audience

- **Russian and Foreign Language Students:** Learners with physical or digital textbooks missing audio components who need to train their listening comprehension.
- **Self-Directed Learners:** Students looking to adjust reading speeds (slow vs. normal voice) to analyze sentence stress (*udarenie*) and phonetics.

## Guiding Principles

- **Zero Perceptible Latency:** Audio generation and playback must leverage in-memory streaming to allow instant listening.
- **Simplicity & Lightness:** The system must require no complex setup or paid API keys, running 100% free with minimal dependencies.
- **Native Phonetic Fidelity:** Priority is given to neural voices that preserve native intonation and stress without robotic distortion.
- **SDD Methodology (Spec-Driven Development):** No code is written without a pre-approved specification (`spec.md`), architectural plan (`plan.md`), and task breakdown (`tasks.md`).

## What it is NOT

- **NOT a mass text editor or full audiobook builder:** It is not designed to process 500-page books in a single background batch.
- **NOT an app with complex user auth or persistence:** It requires no database or user registration in this phase.
- **NOT an offline synthesis tool:** Requires an active internet connection to query Edge-TTS neural voice services.