import cv2
import pytesseract
from PIL import Image
import numpy as np
import argparse
import os

def extract_text_from_video(video_path, timestamps, output_file=None):
    """
    Extract text and screenshots from video frames at specified timestamps
    
    Args:
        video_path (str): Path to the video file
        timestamps (list): List of timestamps (in seconds) to extract text from
        output_file (str): Path to save the output text file
    
    Returns:
        dict: Dictionary with timestamp as key and extracted text as value
    """
    # Initialize video capture
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Dictionary to store results
    text_results = {}
    
    # Create screenshots directory
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    screenshots_dir = f"{video_name}_screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    
    # Sort timestamps to process frames in order
    timestamps = sorted(timestamps)
    
    for timestamp in timestamps:
        # Convert timestamp to frame number
        frame_number = int(timestamp * fps)
        
        if frame_number >= total_frames:
            print(f"Warning: Timestamp {timestamp}s exceeds video duration")
            continue
        
        # Set frame position
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = cap.read()
        
        if ret:
            # Save screenshot
            screenshot_path = os.path.join(screenshots_dir, f"frame_{timestamp:.2f}s.png")
            cv2.imwrite(screenshot_path, frame)
            
            # Convert frame to PIL Image
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
            # Extract text using Tesseract
            text = pytesseract.image_to_string(pil_image)
            
            # Store result whether text was found or not
            text_results[timestamp] = {
                'text': text.strip() if text.strip() else "<NO TEXT DETECTED>",
                'screenshot': screenshot_path
            }
    
    # Release video capture
    cap.release()
    
    # Save results to file if output_file is specified
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            for timestamp, result in text_results.items():
                f.write(f"[{timestamp:.2f}s]\n")
                f.write(f"Text: {result['text']}\n")
                f.write(f"Screenshot: {result['screenshot']}\n")
                f.write("-" * 50 + "\n")  # Separator line
    
    return text_results

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract text and screenshots from video frames at specified timestamps')
    parser.add_argument('video_path', type=str, help='Path to the video file')
    parser.add_argument('--timestamps', type=float, nargs='+', required=True,
                      help='List of timestamps in seconds (e.g., --timestamps 1.5 3.0 5.5)')
    parser.add_argument('--output', type=str,
                      help='Output text file path (default: video_name_extracted.txt)')
    
    args = parser.parse_args()
    
    # Generate default output filename if not provided
    if not args.output:
        video_name = os.path.splitext(os.path.basename(args.video_path))[0]
        args.output = f"{video_name}_extracted.txt"
    
    # Extract text using provided arguments
    results = extract_text_from_video(args.video_path, args.timestamps, args.output)
    
    print(f"Text extraction completed. Results saved to: {args.output}")
    print(f"Screenshots saved in the '{os.path.splitext(os.path.basename(args.video_path))[0]}_screenshots' directory") 