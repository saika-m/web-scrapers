# Web Scraper

This web scraper is designed to extract data from a specific websites.

## List of useful commands:
wget - Complete website mirror with all resources:
```
wget -r -np -k -p -U "Mozilla/5.0" https://example.com
```

curl - Download a single page with all linked content (requires additional processing):
```
curl -L -A "Mozilla/5.0" https://example.com -o example.html
```

httrack - Most comprehensive website mirror:
```
httrack https://example.com -O ./downloaded-site -v -%v
```

aria2 - High-speed download with multiple connections:
```
aria2c -x 16 -s 16 -k 1M https://example.com/file
```

yt-dlp - Best quality video download with all associated content:
```
yt-dlp --write-thumbnail --write-description --write-info-json --all-subs --embed-subs https://www.youtube.com/watch?v=example
```


### Limitations

This web scraper is designed to work with a specific website structure. If the website changes its structure, the scraper may not work as expected. Additionally, some websites may block requests from scripts, so you may need to add additional headers or use a proxy to make the requests appear as if they're coming from a browser.

### Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. You can also report any issues or suggest new features by opening an issue.
