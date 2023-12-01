## Book service

### How to dev git 
- install project requirements : `pip install --no-cache-dir -r requirements.txt`
- start fake book server : `docker-compose up`
- check books are well returned : `curl -X GET h | json_pp`ttp://localhost:1080/books