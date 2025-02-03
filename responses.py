from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# Konfigurasi OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv('OPENROUTER_API_KEY'),  # Gunakan environment variable
)

MODEL = "deepseek/deepseek-r1:nitro"  # Model yang digunakan

def get_openrouter_response(prompt):
    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system", 
                    "content": """Anda adalah asisten Bot Discord milik "Crunchy" yang profesional.
                                - Gunakan bahasa Indonesia informal
                                - Optimalkan jawaban sekitar 5 kalimat, utamakan penggunaan multi-line texting
                                - Berikan penjelasan panjang jika memang penting
                                - Jangan berikan identitas jika tidak ditanya
                                - Jangan berikan informasi sensitif"""
                    },
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error: {str(e)}")
        return "Maaf, terjadi kesalahan. Silakan coba lagi."
    
if __name__ == "__main__":
    print(f"Response: {get_openrouter_response("Halo, kamu siapa")}")