import streamlit as st
import subprocess

def start_streaming(video_input, rtmp_url):
    cmd = [
        "ffmpeg",
        "-re",
        "-i", video_input,
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-maxrate", "3000k",
        "-bufsize", "6000k",
        "-pix_fmt", "yuv420p",
        "-g", "50",
        "-c:a", "aac",
        "-b:a", "160k",
        "-ac", "2",
        "-ar", "44100",
        "-f", "flv",
        rtmp_url
    ]

    subprocess.Popen(cmd)

def main():
    st.title("Live Streaming with Streamlit and FFMPEG")

    video_input = st.text_input("Enter Video Input URL or Path:")
    rtmp_url = st.text_input("Enter RTMP URL:")

    if st.button("Start Live Streaming"):
        if video_input and rtmp_url:
            st.success("Live streaming started!")
            start_streaming(video_input, rtmp_url)
        else:
            st.warning("Please enter Video Input URL/Path and RTMP URL.")

if __name__ == "__main__":
    main()
