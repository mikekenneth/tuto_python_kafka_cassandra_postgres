<h1 align="center">Python Kafka Cassandra Postgresql Tutorial</h1>

## What is it?
Data Engineering Project: Consumer data from Kafka and insert in to cassandra &amp; postgresql databases. There is also some data enrichement

## Use Case
In this use case we are to get data from kafka broker (consuming) and inserting into databases (Cassandra & PostgreSQL) simultaeniously


## How does it work?
### Initialization
Before we start the project, we need to update the ".conf_sample.ini" file that holds configurations. Then remane it to ".conf.ini"

## How to use it?

```python
python3 initialize_database.py
```

## TODO

- [ ] Add other data pipeline tools in the design and see how they work together.
- [ ] Design a website to monitor all the pipeline & Trigger Data Generation
    - [ ] Kafka topics messages stats: 
    - [ ] Records in cassandra & postgresql tables

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

See as you fit.

## Contact

If you have any questions or would like to get in touch, please open an issue on Github or send me an email: <mike.kenneth47@gmail.com>
