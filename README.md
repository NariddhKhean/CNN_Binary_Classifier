# CNN_Classifier

Web scrape images based on a lists of _Google Images_ search queries, to generate a training dataset for classification. Train and save a deep convolutional neural network. Load the trained model to classify new images from an image's url.

> _"Apples are red with thin, edible skin, and white flesh. Whereas oranges are rounder, with orange-coloured skin and orange-coloured flesh. And the skin of an orange is generally discarded before consumption. You know what just happened there? I just compared apples to oranges. It can be done!"_
>
> \- Ronny Chieng.

## Getting Started

### Prerequisites

The main component of the web scraper is _[Google Images Download](https://github.com/hardikvasa/google-images-download)_; a small, ready-to-run program that downloads images from a Google Images search from keywords.
> Note: If you would like to scrape more than 100 images per keyword, you'll also need to install _[Selenium](https://www.seleniumhq.org/)_ and _[Chromedriver](http://chromedriver.chromium.org/)_.

The deep convolutional neural network was developed using _[TensorFlow](https://www.tensorflow.org/)_.

To install _Google Images Download_ and TensorFlow, you can use pip:
```
pip install google_images_download
```
```
pip install tensorflow
```
Alternatively, you can view their respective documentation for different installation methods and troubleshooting.

To install TensorFlow, it's best to refer to their [documentation](https://www.tensorflow.org/install/).
> Note: To considerably speed up training time, install TensorFlow with GPU support.

## Usage

### `config.json`

| Variable            | Function                                                                      |
| ------------------- | ----------------------------------------------------------------------------- |
| `search_terms`      | List of search terms to web scrape.                                           |
| `scrape_limit`      | Maximum number of images that the script will attempt to scrape.              |
| `training_factor`   | Ratio for training images to validation images.                               |
| `target_size`       | Target pixel width and height of training images.                             |
| `batch_size`        | Number of images within a batch.                                              |
| `epochs`            | Number of times the model trains on each image.                               |

### `web_scraper.py`

`web_scraper.py` iterates through the list of search terms defined in the configuration file, attempts to downloads the images, and saves it onto your drive. The downloaded images are then divided into a training dataset and a validation dataset.

### `cnn_train.py`

`cnn_train.py` preprocesses the training images, trains the deep convolutional neural network, and then saves the trained model. After training, the model will be saved, again onto the user's desktop into a folder called 'model'.

### `model_predict.py`

`model_predict.py` loads the trained model based on the directory defined in the configuration file, to predict the class of a new image. This can be run using the shell command, where 'url' is the url of the image:
```
python model_predict.py url
```
For example:
```
python model_predict.py https://charliesfruitonline.com.au/wp-content/uploads/2017/01/apples.jpg
```
