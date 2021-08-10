# Copyright (c) 2021 - Itz-fork
# Project: py_extract
import json
import os

from .helpers import run_cmd

class Video_tools():
    def video_info(input_file):
        if input_file is None:
            return {"error": "input_file must not be None"}
        else:
            pass
        try:
            cmd = f"ffprobe -show_format -show_streams -loglevel quiet -print_format json {input_file}"
            json_d = run_cmd(cmd)
            return json_d
        except Exception as error:
            return {'error': error}
    
    def extract_all_audio(input_file=None, output_path=None):
        input_file = input_file
        output_path = output_path
        if input_file is None:
            return {"error": "input_file must not be None"}
        elif output_path is None:
            output_path = "py_extracted/all_audios"
        # Creating directories if not exist
        if os.path.exists(output_path):
            out_path = output_path
        else:
            os.makedirs(output_path)
            out_path = output_path
        try:
            json_details = Video_tools.video_info(input_file)
            details = json.loads(json_details)
            for toextract in details['streams']:
                the_mapping = toextract['index']
                codec_name = toextract['codec_name']
                codec_type = toextract['codec_type']
                if codec_type in ("audio"):
                    pass
                else:
                    continue
                for audio in codec_name:
                    out_audio = f"{out_path}/extracted_{codec_type}_{the_mapping}.{codec_name}"
                    cmd = f"ffmpeg -i {input_file} -map 0:{the_mapping} -c copy {out_audio} -y"
                    run_cmd(cmd)
                print("Process Finished")
            return [os.path.abspath(out_path) for file in os.listdir(out_path)]
        except Exception as error:
            return {"error": error}
    
    def extract_first_audio(input_file=None, output_path=None):
        input_file = input_file
        output_path = output_path
        if input_file is None:
            return {"error": "input_file must not be None"}
        elif output_path is None:
            output_path = "py_extracted/one_audio"
        # Creating directories if not exist
        if os.path.exists(output_path):
            out_path = output_path
        else:
            os.makedirs(output_path)
            out_path = output_path
        # Get audio codec
        try:
            data = Video_tools.video_info(input_file)
            json_data = json.loads(data)
            # Extracting first audio of a video
            audio_type = json_data['streams'][1]['codec_name']
            out_file = f"{out_path}/py_extracted_audio.{audio_type}"
            # Extracting audio
            cmd = f"ffmpeg -i {input_file} -vn -acodec copy {out_file}"
            run_cmd(cmd)
            return out_file
        except Exception as error:
            return {"error": error}