# 🧘 Recovery Dharma Costa Mesa

This project is an informational website for the **Recovery Dharma Costa Mesa** group, which follows a mindfulness-based approach to the path to recovery. The application was built with **Python (Flask)** and is deployed on **Render**.

## 📌 Visit the website

🌐 [https://recovery-dharma-costa-mesa.onrender.com](https://recovery-dharma-costa-mesa.onrender.com)

---

## 💡 Objective

To provide a simple and accessible online presence so that members and new participants can find information about:

- What is Recovery Dharma
- Available meetings
- Contact
- Useful resources for recovery

---

## 🛠️ Technologies used

- **Python**: Main back-end language
- **Flask**: Microframework to create the web application
- **HTML + CSS**: To structure and style the pages
- **Gunicorn**: WSGI server to deploy on Render
- **Render**: Hosting platform used to deploy the application


---

## ⚙️ How to run locally

> Requires: Python 3.11+ and pip

1. Clone the repository

```bash
git clone https://github.com/ThayRibeiro0/recovery_dharma-costa-mesa.git
cd recovery_dharma-costa-mesa
```

2. Create and activate an environment virtual

```bash
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
Start the local server
```

```bash
flask run
Access it at: http://localhost:5000
```

## 🚀 Deploy

The application is hosted on Render as a web service. Deployment is done automatically when you push to the main branch.

Production Commands

1. Build Command:

```bash
pip install -r requirements.txt
```

2. Start Command:

```bash
gunicorn app:app
```

## 📬 Contact
For more information, suggestions or contributions, please contact:
📧 thaysmoiaribeiro@gmail.com

## 🧘 About Recovery Dharma
Recovery Dharma is an approach based on meditation practices, Buddhist wisdom and mutual support. The community offers support for anyone seeking recovery from addiction and suffering, in an inclusive and compassionate environment.

## 📝 License
This project is open source and is under the MIT license.
**
