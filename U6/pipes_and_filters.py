import sqlparse


class TokenizeFilter:
    def process(self, input_data):
        tokens = sqlparse.parse(input_data)[0].tokens
        return tokens


class ParseFilter:
    def process(self, input_tokens):
        parsed_statement = sqlparse.sql.Statement(input_tokens)
        return parsed_statement


class PrintFilter:
    def process(self, input_tokens):
        for token in input_tokens:
            print(token.value)
        return input_tokens


class ElimFilter:
    def process(self, input_tokens):
        tokens = [
            token
            for token in input_tokens
            if not token.value.lower().startswith("where")
        ]
        return tokens


class SQLParserPipeline:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter_instance):
        self.filters.append(filter_instance)

    def run_pipeline(self, input_data):
        data = input_data
        for filter_instance in self.filters:
            data = filter_instance.process(data)


if __name__ == "__main__":
    # Example SQL statement
    sql_statement = "SELECT * FROM my_table WHERE column = 'value';"

    # Create pipeline
    pipeline = SQLParserPipeline()
    pipeline.add_filter(TokenizeFilter())
    pipeline.add_filter(ParseFilter())
    pipeline.add_filter(PrintFilter())
    pipeline.add_filter(ElimFilter())
    pipeline.add_filter(PrintFilter())

    # Run pipeline
    pipeline.run_pipeline(sql_statement)
