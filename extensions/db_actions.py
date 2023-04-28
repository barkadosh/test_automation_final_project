import allure
import test_cases.conftest as conf

class DBActions:
    @staticmethod
    @allure.step('Query Builder - WHERE statement')
    # Example: "# SELECT user, password, From usersfinalprojectaut WHERE comments = 'correct'"
    def query_builder(columns, table, where_name, where_value):
        cols = ','.join(columns)
        query = f'SELECT {cols} FROM {table} WHERE {where_name} = {where_value};'
        return query

    @staticmethod
    @allure.step('Get query result')
    def get_query_result(columns, table, where_name, where_value):
        query = DBActions.query_builder(columns, table, where_name, where_value)
        db_cursor = conf.db_connector.cursor()
        db_cursor.execute(query)
        result = db_cursor.fatchall()
        return result
