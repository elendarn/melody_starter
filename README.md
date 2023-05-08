# Melody Starter
## Music Generation with Generative AI

## Overview
Melody Starter is a music generation project that focuses on composing melodies from given sequences of notes for smart instruments. The model is trained using classical piano pieces from 254 songs by 17 famous composers, including Beethoven, Bach, and Mozart. The project aims to generate melodies by anticipating the sequence of notes without considering timing, duration, or timbre initially. The method employed is a Convolutional Neural Network (CNN) with WaveNet deep learning, which has been successfully used by Google voice recognition services since 2017.

## Dataset
The model is trained on a dataset consisting of classical piano pieces from MIDI files. The dataset comprises 254 songs by 17 renowned composers, providing a diverse range of musical styles and compositions. The MIDI files are processed using the Music21 and Mido packages, which extract the songs into sequences of notes. This allows the model to learn the patterns and structure of classical piano music.

## Methodology
The music generation process is a high-dimensional and complex task. Therefore, Melody Starter focuses on the initial stage of anticipating a sequence of notes without considering other musical elements. The model is trained to predict the subsequent note based on the given notes in the sequence. The CNN with WaveNet architecture is employed for this task, as it excels in capturing long-term dependencies in sequential data.

The code follows a two-step process:
1. Extracting songs from MIDI files and converting them into sequences of notes using the Music21 and Mido packages.
2. Training the model with the extracted sequences to predict the melody. The sequences are cut into equal pieces, and the model is trained to predict the next note based on the previous notes.

In the first step, the subsequent note is predicted based on the given notes. In the second step, the prediction is added to the end of the input sequence, becoming the one previous note for the next prediction. This process is repeated until there are no more given notes left in the sequence. Two models, with similar CNN WaveNet structures, are created, differing only in the packages used for the extraction process and the structure of the sequence.

## Usage
To use Melody Starter, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies, including Python (version X.X.X), TensorFlow (version X.X.X), and any other specified libraries.
3. Run the code and explore the implementation details.
4. Provide a sequence of notes as input and use the model to generate a melody based on the given notes.
5. Experiment with different input sequences and explore the variety of melodies that can be generated.

## Acknowledgements
This project would not have been possible without the contributions of the open-source libraries Music21 and Mido, which were used for extracting songs from MIDI files and converting them into sequences of notes. The classical piano pieces used in the dataset were obtained from various sources and encompass compositions by 17 famous composers, including Beethoven, Bach, and Mozart. Their timeless music serves as the foundation for the model's learning and music generation.
