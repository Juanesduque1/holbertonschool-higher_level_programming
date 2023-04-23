# Object-relational mapping
Project done during my **Software Engineering studies** at **Holberton School**. It aims to learn about how to connect to a `MySQL` database from a **Python script**, what `ORM` means and how to map a Python Class to a `MySQL` table.

## Files
| Filename | Description |
| -------- | ----------- |
| [`0-select_states.py`](./0-select_states.py) | Lists all `states` from the database `hbtn_0e_0_usa`. |
| [`1-filter_states.py`](./1-filter_states.py) | Lists all `states` with a `name` starting with `N` from the database `hbtn_0e_0_usa`. |
| [`2-my_filter_states.py`](./2-my_filter_states.py) | Takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. |
| [`3-my_safe_filter_states.py`](./3-my_safe_filter_states.py) | Takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument without injection. |
| [`4-cities_by_state.py`](./4-cities_by_state.py) | Lists all `cities` from the database `hbtn_0e_4_usa`. |
| [`5-filter_cities.py`](./5-filter_cities.py) | Takes in the name of a state as an argument and lists all `cities` of that state. |
| [`6-model_state.py`](./6-model_state.py) | Contains the class definition of a `State` and an instance `Base = declarative_base()`. |
| [`7-model_state_fetch_all.py`](./7-model_state_fetch_all.py) | Lists all `State` objects from the database `hbtn_0e_6_usa`. |
| [`8-model_state_fetch_first.py`](./8-model_state_fetch_first.py) | Prints the first `State` object from the database `hbtn_0e_6_usa`. |
| [`9-model_state_filter_a.py`](./9-model_state_filter_a.py) | Lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`. |
| [`10-model_state_my_get.py`](./10-model_state_my_get.py) | Prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`. |
| [`11-model_state_insert.py`](./11-model_state_insert.py) | Adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`. |
| [`12-model_state_update_id_2.py`](./12-model_state_update_id_2.py) | Script that changes the name of a `State` object from the database `hbtn_0e_6_usa`. |
| [`13-model_state_delete_a.py`](./13-model_state_delete_a.py) | Script that deletes all `State` objects with the name containing the letter `a` from the database `hbtn_0e_6_usa`. |
| [`14-model_city_fetch_by_state.py`](./14-model_city_fetch_by_state.py) | Prints all `City` objects from the database `hbtn_0e_14_usa`. |
| [`model_city.py`](./model_city.py) | Contains the class definition of a `City`, which inherits from `Base`. |
| [`model_state.py`](./model_state.py) | Contains the class definition of a `State` with a relationship with the class `City`. |

## Authors

* Juan Esteban Duque <a href="https://github.com/Juanesduque1" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>