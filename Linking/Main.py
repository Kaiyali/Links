import tkinter as tk
import tkinter.filedialog as filedialog
import pytube as utube


class Links:
    def __init__(self, root):
        self.root = root
        root.title("linking")
        self.label = tk.Label(root, text="No path selected")
        self.button = tk.Button(
            root, text="Select folder", command=self.select_path)
        self.textbox = tk.Entry(root)
        self.download_type = tk.StringVar()
        self.download_type.set("audio")
        self.radio_audio = tk.Radiobutton(
            root, text="Audio", variable=self.download_type, value="audio")
        self.radio_video = tk.Radiobutton(
            root, text="Video", variable=self.download_type, value="video")
        self.download_button = tk.Button(
            root, text="Download", command=self.download_video)
        self.label.grid(row=0, column=0)
        self.button.grid(row=0, column=1)
        self.textbox.grid(row=1, column=0)
        self.radio_audio.grid(row=2, column=0)
        self.radio_video.grid(row=2, column=1)
        self.download_button.grid(row=3, column=0, columnspan=2)

    def select_path(self):
        path = filedialog.askdirectory()
        self.label.config(text=path)

    def download_video(self):
        url = self.textbox.get()
        try:
            yt = utube.YouTube(url)
            download_type = self.download_type.get()

            if download_type == "audio":
                stream = yt.streams.filter(only_audio=True).get_audio_only()
            else:
                stream = yt.streams.get_highest_resolution()

            path = self.label['text']

            try:
                stream.download(path)
                tk.messagebox.showinfo(
                    "Download complete", "The video or audio has been downloaded to the selected path")
            except IOError:
                tk.messagebox.showerror(
                    "Error", "Unable to write to the specified path")
        except utube.exceptions.RegexMatchError:
            tk.messagebox.showerror("Error", "Invalid YouTube URL")
        except utube.exceptions.VideoUnavailable:
            tk.messagebox.showerror("Error", "Video unavailable")


root = tk.Tk()
app = Links(root)
root.mainloop()
