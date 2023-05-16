from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


engine = create_engine('sqlite:///game.db', echo=True)
metadata = MetaData()


questions = Table('questions', metadata,
    Column('id', Integer, primary_key=True),
    Column('question', String),
    Column('answer', String),
    Column('hint', String),
    Column('score', Integer)
)

metadata.create_all(engine)
conn = engine.connect()

# insert five rows into the questions table
conn.execute(questions.insert(), [
    {'question': 'What is the capital of France?', 'answer': 'Paris', 'hint': 'It starts with a "P"', 'score': 100},
    {'question': 'Who wrote "To Kill a Mockingbird"?', 'answer': 'Harper Lee', 'hint': 'Her first name is Nelle', 'score': 200},
    {'question': 'What year did World War II end?', 'answer': '1945', 'hint': 'It was after 1940', 'score': 300},
    {'question': 'What is the smallest country in the world?', 'answer': 'Vatican City', 'hint': 'It is an independent city-state', 'score': 400},
    {'question': 'What is the highest mountain in Africa?', 'answer': 'Mount Kilimanjaro', 'hint': 'It is located in Tanzania', 'score': 500}
])
conn.commit()
conn.close()

# retrieve the rows from the questions table

