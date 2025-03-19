import re

def extract_data(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        name_pattern = r'<div class="d4r55 ">([^<]+)</div>'
        stars_pattern = r'<span class="kvMYJc" role="img" aria-label="(\d+) 顆星">'
        time_ago_pattern = r'<span class="rsqaWe">([^<]+)</span>'
        comments_pattern = r'<span class="wiI7pd">([^<]+)</span>'
        
        names = re.findall(name_pattern, text)
        stars = re.findall(stars_pattern, text)
        times_ago = re.findall(time_ago_pattern, text)
        comments = re.findall(comments_pattern, text)
        
        data = {
            'name': names if names else None,
            'stars': stars if stars else None,
            'time_ago': times_ago if times_ago else None,
            'comments': comments if comments else None
        }
        
        with open('output.md', 'w') as output_file:
            for i in range(min(len(names), len(times_ago), len(stars), len(comments))):
                output_file.write(f'# num{i+1}\n{names[i]}\n')
                output_file.write(f'{times_ago[i]}\n\n')
                output_file.write(f'Stars: {stars[i]}\n\n')
                output_file.write(f'{comments[i]}\n\n')

file_path = 'input.txt'
extract_data(file_path)
