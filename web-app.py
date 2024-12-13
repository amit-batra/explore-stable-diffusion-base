import streamlit as st
import torch
from diffusers import DiffusionPipeline, DDIMScheduler

# Function to Load and Cache the AI Model
@st.cache_resource(show_spinner="Loading the model...")
def load_model():
	model_name = "stabilityai/stable-diffusion-xl-base-1.0"

	# Load the model with FP16 precision and SafeTensors
	pipeline = DiffusionPipeline.from_pretrained(
		model_name,
		torch_dtype=torch.float16,
		use_safetensors=True,
		variant="fp16"
	).to("mps")

	# Replace the default scheduler with DDIM for faster inference
	pipeline.scheduler = DDIMScheduler.from_config(pipeline.scheduler.config)

	return pipeline

# The Main Function is invoked by Streamlit whenever the web-page is rendered
def main():

	# Title of the web app
	st.title("Image Generator")

	# Optionally Load and Cache the model
	# If the model is already cached, this will be skipped
	pipeline = load_model()

	# Section: Pre-generated prompt suggestions
	st.subheader("Try a Pre-Generated Prompt")
	suggestions = [
		"A futuristic city with flying cars at sunset",
		"A magical forest with glowing mushrooms and fairies",
		"An astronaut riding a horse on Mars",
		"A cozy cabin in a snowy landscape under northern lights"
	]
	pre_selected_prompt = st.selectbox("Select a prompt:", [""] + suggestions)

	# Text input for the user
	st.subheader("Or Enter Your Own Prompt")
	user_input = st.text_area("Describe the image:")

	# Use selected prompt if user input is empty
	if pre_selected_prompt and not user_input:
		user_input = pre_selected_prompt

	# Slider to allow the user to adjust timesteps for faster generation
	num_steps = st.slider("Number of Timesteps (Lower = Faster, Less Accurate)", min_value=10, max_value=50, value=20)

	# Slider to allow the user to adjust the guidance scale
	guidance_scale = st.slider("Guidance Scale (Higher = Closer to Prompt)", min_value=5.0, max_value=15.0, value=7.5)

	# Button to trigger image generation
	if st.button("Generate"):
		# If nothing in prompt, then show an error message
		if not user_input:
			st.error("Please enter a prompt.")
		else:
			# Start a spinner
			with st.spinner("Generating images..."):
				# Generate image(s) from the user input
				# pipeline.scheduler.set_timesteps(num_steps) # Adjust the timesteps dynamically
				images = pipeline(prompt=user_input, num_inference_steps=num_steps, guidance_scale=guidance_scale).images

			# After the spinner is done, display the image(s)
			st.caption("Generated Images")
			# for image in st.session_state.images:
			for image in images:
				st.image(image, use_container_width=True)

if __name__ == "__main__":
	main()