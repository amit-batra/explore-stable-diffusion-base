# Text to Image using Stability AI's Stable Diffusion Base Model
This application uses Stability AI's Stable Diffusion Base Model combined with Hugging Face's Python diffusion client to convert text to an image.

# Running Locally
You need the following on your machine to run this app locally:
1. Clone this repository: `git clone git@github.com:amit-batra/explore-stable-diffusion-base.git`.
2. Ensure that you have a functional Python 3 installation (we tested this app with Python 3.12). On macOS, you can use Homebrew to install Python 3.12 like so: `brew install python@3.12`.
3. Create a Python virtual environment and activate it with these commands:
   1. `cd explore-stable-diffusion-base`
   2. `python3 -m venv .venv`
   3. `source .venv/bin/activate`
4. At this point, you should see the name of the virtual environment printed in brackets `(.venv)` before your actual command prompt.
5. Now install the required Python libraries inside your virtual environment with these commands:
   1. `pip install --upgrade pip`
   2. `pip install streamlit torch diffusers watchdog transformers accelerate`
6. Launch the web-app using this command: `streamlit run web-app.py`. When you do this for the first time, the Hugging Face diffusion Python client library will download the Stable Diffusion Base Model for you and cache it on your disk. This operation might take a couple of minutes. The next time onwards, the cached version of the model will be loaded from the disk directly.
7. Streamlit should automatically open the web-app in your default browser. If this does not happen, manually navigate to this web-page: http://localhost:8501.
8. Try out various prompts and play around with the other input parameters that control the image generation.
9. After you are done, kill the Python interpreter and then deactivate your Python virtual environment using the command `deactivate`.