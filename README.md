# 🎶 Zero Touch Lofi

**Zero Touch Lofi** is a fully automated platform designed to generate, visualize, and upload **1-hour lo-fi music videos** to YouTube with zero manual intervention. Leveraging AI-driven automation, scheduling, and workflow orchestration, it allows creators, YouTube channels, and enthusiasts to maintain a consistent presence on the platform effortlessly.

Whether you're a solo content creator looking to scale your output, a developer exploring AI-powered automation, or a YouTube channel aiming for regular uploads, Zero Touch Music handles the entire pipeline end-to-end.

---

# 🚀 Overview

Zero Touch Music is engineered to manage the complete content creation and publishing process automatically:

1. **Audio Generation**  
   - Produces high-quality, royalty-free 1-hour lo-fi beats suitable for streaming, study, or relaxation.  
   - Supports configurable BPM, mood, and audio styles.

2. **Video Production**  
   - Automatically generates visually appealing videos to accompany audio.  
   - Includes smooth looping visualizers, animations, or custom backgrounds.  
   - Adjustable resolution and frame rate to meet YouTube quality standards.

3. **YouTube Upload**  
   - Directly uploads generated videos using the YouTube Data API.  
   - Automatically populates optimized metadata including:  
     - Video titles  
     - Descriptions  
     - Tags  
     - Thumbnails  
   - Ensures better discoverability and SEO optimization for your channel.

4. **Email Notifications**  
   - Sends automatic confirmations for uploads and system events.  
   - Default notification email: `zerotouchai.official@gmail.com`.

5. **Scheduling & Automation**  
   - Allows fully zero-touch publishing at predefined intervals.  
   - Enables channels to maintain a consistent content cadence without manual intervention.

---

# ✨ Key Features

- ✅ **End-to-End Automation** – From audio generation to publishing, everything runs automatically.  
- ✅ **Professional Metadata Handling** – Optimized YouTube-friendly titles, descriptions, and tags.  
- ✅ **Customizable Video Output** – Adjustable resolutions, visualizer styles, and themes to match your branding.  
- ✅ **Integrated Email Alerts** – Receive notifications for successful uploads, failures, or system events.  
- ✅ **Scalable & Efficient** – Perfect for personal projects, educational purposes, or professional YouTube channels.  
- ✅ **Configurable Scheduler** – Set your own publishing intervals and timezone to maintain consistency.  

---

# 🛠 Requirements

Before running Zero Touch Music, ensure your environment meets the following requirements:

- Python 3.9 or higher  
- YouTube Data API credentials (with OAuth 2.0 setup)  
- SMTP-enabled email account for notifications  
- FFmpeg installed and added to system PATH  
- Internet connection for API access and uploads  

---

# ⚙️ Installation & Setup

Follow these steps to set up Zero Touch Music:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/zero-touch-music.git
cd zero-touch-music
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Credentials

Set up:

- YouTube API keys and OAuth client secrets  
- Email SMTP credentials  
- Video, metadata, and scheduling settings  

⚠️ **Never commit secrets or API keys** to the repository. Use environment variables or a secure `.env` file.

### 5️⃣ Run the Uploader

```bash
python main.py
```

Once started, the system will automatically generate music, create videos, and upload content based on your configuration.

---

# 📂 Configuration Options

Zero Touch Music is highly configurable:

## 🎥 Video Settings
- Resolution: e.g., 1920x1080, 1280x720  
- Frame rate: e.g., 30fps, 60fps  
- Visualizer style: bars, waves, or custom animations  
- Background theme and colors  

## 📝 Metadata Settings
- Title template  
- Description template  
- Tags  
- Thumbnail image selection  

## ⏱ Scheduler
- Upload intervals  
- Scheduled publish time  
- Timezone configuration  

## 📧 Email Notifications
- Sender and recipient email credentials  
- Alerts for success, failure, or errors  

---

# 🤝 Contributing

We welcome contributions from developers, designers, and community members!  

See the full [Contributing Guidelines](CONTRIBUTING.md) for:

- Branching and pull request instructions  
- Coding standards and best practices  
- Issue reporting and discussion etiquette  

Whether it’s adding new features, fixing bugs, or improving documentation, your contributions are appreciated.

---

# 🛡 Security

Security is important to us. Please follow the [Security Policy](SECURITY.md) for:

- Reporting vulnerabilities responsibly  
- Handling sensitive credentials  
- Best practices for safe usage  

Do not create public issues for security concerns—use the secure reporting guidelines.

---

# 📜 Code of Conduct

All participants in the project must adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) to maintain a safe, inclusive, and respectful community.  

Key points include:

- Be respectful and constructive in communication  
- Avoid harassment, discriminatory language, or personal attacks  
- Report issues with civility and professionalism  

---

# 📌 License

This project is licensed under the **Apache License 2.0**.  
See the [LICENSE](LICENSE) file for full details.

Key points:

- Use, modify, and distribute freely under the license  
- Include a copy of the license in derivative works  
- No warranty or liability is provided  

---

# 📧 Contact

For questions, support, or collaborations:

- Email: [zerotouchai.official@gmail.com](mailto:zerotouchai.official@gmail.com)  
- GitHub Discussions: Engage with the community, report issues, or suggest features  

---

# ⚠️ Disclaimer

Users are responsible for:

- Complying with YouTube Terms of Service  
- Ensuring generated content adheres to copyright regulations  
- Safeguarding API credentials and account security  

The maintainers are **not responsible** for misuse, copyright violations, or account penalties.

---

🚀 **Build once. Automate forever.**
