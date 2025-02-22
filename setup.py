from setuptools import setup, find_packages

setup(
    name="file-meta",                      
    version="0.1",                         
    packages=find_packages(),              
    install_requires=[                    
        "Pillow",
        "moviepy",
        "PyPDF2",
        "mutagen",
    ],
    classifiers=[                          
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',               
)

