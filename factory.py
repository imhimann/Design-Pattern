#Video Exporting Example

from email.mime import audio
import pathlib
from abc import ABC, abstractmethod

class VideoExporter(ABC):
    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting"""
        
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""
        
class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec"""
    
    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video in lossless format to {folder}.")
    

class H264BVideoExporter(VideoExporter):
    """H.264 video exporting codec"""
    
    def prepare_export(self, video_data):
        print("Preparing video data for H.264 export.")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 format to {folder}.")
        
class H264Hi422PVideoExporter(VideoExporter):
    """H.364 video exporting odec with Hi422P profile"""
    
    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")
        
        

class AudioExporter(ABC):
    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""
        
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""
        
class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""
    
    
    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")
        
class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec"""
    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")
        
def main() -> None:
    """Main function"""
    
    #read the export quality
    export_quality: str
    while True:
        export_quality = input("Enter desired output quality: ")
        if export_quality in {"low", "high", "master"}:
            break
        print(f"Unknown output quality option: {export_quality}")
        
    #create the video and audio exporters
    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    
    if export_quality == "low":
        video_exporter = H264BVideoExporter()
        audio_exporter = AACAudioExporter()
        
    elif export_quality == "high":
        video_exporter = H264Hi422PVideoExporter()  
        audio_exporter = AACAudioExporter() 
    else:
        video_exporter = LosslessVideoExporter()
        audio_exporter = WAVAudioExporter()
        
        
    #prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")
    
    #do the export
    folder = pathlib.Path("/u (variable) folder: pathlib.Path")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)
    

if __name__ == "__main__":
    main()
        
        
        
        
        