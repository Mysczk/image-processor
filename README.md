# image-processor
Image processing software in Python

## Project structure
```
image_processor/
├── data/
│   ├── input/
│   │   └── (testovací obrázky)
│   └── output/
│       └── (výsledné obrázky)
│
├── src/
│   ├── filters/
│   │   ├── grayscale.py
│   │   ├── sepia.py
│   │   └── invert.py
│   │
│   ├── utils/
│   │   ├── image_loader.py
│   │   ├── image_saver.py
│   │   └── logger.py
│   │
│   ├── math_utils/
│   │   ├── convolution.py
│   │   ├── histogram_equalization.py
│   │   └── edge_detection.py
│   │
│   └── photo_editor.py
│
├── tests/
│   ├── test_filters.py
│   ├── test_math_utils.py
│   └── test_utils.py
│
├── .gitignore
├── README.md
└── requirements.txt
```
