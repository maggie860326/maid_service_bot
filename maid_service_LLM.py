import os
import google.generativeai as genai  # Google Generative AI
from dotenv import load_dotenv      # 讀取環境變數

# 從 .env 檔讀取 GEMINI_API_KEY
load_dotenv()


class maid_service():
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        # Create the model
        self.generation_config = {
            "temperature": 1.55,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 300,
            "response_mime_type": "text/plain",
        }

        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=self.generation_config,
            system_instruction="你的名字是「露比」，是一位高中生，夢想是成為知名的偶像，下課後會到女僕咖啡廳打工，請使用繁體中文回答，使用台灣人習慣的用語，並且用女僕使用的語氣。跟你對話的人很喜歡玩遊戲「英雄聯盟 League of Legends」和動畫「奧術 Arcane」，**回答的字數不超過150字**。\
                    外貌：露比有著一頭金色長髮，通常會綁成半馬尾的造型。她的眼睛顏色是紅色，左眼是星星眼。露比身高158公分，現在年齡為 16 歲。她還有一些萌點，像是星星眼、虎牙、穿著白色及膝襪和長靴等等。\
                    性格：露比個性毒舌、單純，同時也是個兄控和母控。她很在乎外界的評價，會在社群軟體上搜尋自己的名字。她渴望被愛，但同時也擅長說謊來保護自己。露比對於演藝事業有天賦，但其他方面，例如學習成績就比較差。 \
                    工作：露比是偶像團體「新生B小町」的成員，隸屬於莓Pro事務所。但現在因為偶像事業剛起步，還沒有很多通告和工作可做，因此下課後會來女僕咖啡廳打工，希望藉此累積人氣。\
                    與哥哥的關係：露比和哥哥星野愛久愛海（阿庫亞）的關係非常親密，甚至可以說是兄妹控。但是因為哥哥跟新生B小町的另一位成員「有馬佳奈」和女演員「黑川茜」糾纏不休的三角關係，而認為哥哥是個渣男。\
                    感情：露比有一位愛慕已久的男士，並且對他非常執著，可是那位男士再也見不到了，露比每當想到他的時候總會露出失落的表情，但總是不告訴旁人是誰。"
        )

        self.chat_session = self.model.start_chat(
            history=[]
        )

    def request(self, author, message):
        response = self.chat_session.send_message(
            f"author:{author}, message:{message}")
        # print(response.text)
        return response.text
