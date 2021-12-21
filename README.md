# Non-Fungible Token (NFT) Authenticity using Sentiment Analysis

## Research Paper
Our research paper can be viewed [here](https://github.com/taradactyl27/nft-sentiment-analysis/blob/main/paper/NLP_Paper.pdf)

## Installation

1. Clone the repository 
    
    `git clone git@github.com:taradactyl27/nft-sentiment-analysis.git`
2. All code is located within the nftsentiment.ipynb Jupyter Notebook. This can be viewed within Google Colab, VS Code, or whichever way is most convenient for you.
   
## Requirements

1. Transaction scraping from OpenSea requires an API key that can be obtained by applying for it in the OpenSea API documentation. The key should be placed in a .env file in the following format:

    `OPENSEA_API_KEY=YOUR_KEY_HERE`

2. Twitter scraping also requires authorization credentials that can be acquired by applying for them in the Twitter API documentation. These credentials will also be placed in a .env file with the following format:

    `CONSUMER_KEY=YOUR_CONSUMER_KEY`
    `CONSUMER_SECRET=YOUR_CONSUMER_SECRET` 
    `ACCESS_TOKEN=YOUR_ACCESS_TOKEN`
    `ACCESS_TOKEN_SECRET=YOUR_ACCESS_TOKEN_SECRET`

## Project Layout

- `data/`: All scraped tweets will be located in this folder.
- `features.csv`: This is the main features file that is used as input for data preprocessing before being inputted to models.
- `collections.csv`: This is the list of NFT collections that we compiled and labeled. Additional projects can be added, and we encourage you to add, following the format inside the file.
- `nftsentiment.ipynb`: Main Jupyter Notebook