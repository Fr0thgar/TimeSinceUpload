from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/latest-upload/<channel_id>', methods=['GET'])
def get_latest_upload(channel_id):
    url = f"https://www.youtube.com/@MichaelReeves/videos"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    
    soup = BeautifulSoup(response.content, 'html.parser')
    latest_video = soup.find('a', {'id': 'video-title'})
    
    if latest_video:
        publish_date = latest_video.find('div', {'class': 'style-scope ytd-grid-video-renderer'}).text.strip()
        return jsonify({'publish_date': publish_date})
    else:
        return jsonify({'error': 'No videos found'}), 404

if __name__ == '__main__':
    app.run(debug=True)