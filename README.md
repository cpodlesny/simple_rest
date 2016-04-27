1. git clone https://github.com/cpodlesny/simple_rest.git;
2. cd simple_rest;
3. docker-machine start default;
4. docker-machine env default;
5. eval $(docker-machine env default);
6. docker-compose up --build;
7. docker ps // Check id of web container;
8. docker exec -it <id web container> bash;
9. Run python manage.py <django commands> from <id web container> 
10. Run pip freeze to check project dependencies 
