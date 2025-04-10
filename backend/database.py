from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import UniqueConstraint


# Connect to SQLite database
DATABASE_URL = "sqlite:///./bike_setup.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Stem(Base):
    __tablename__ = "stems"
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    length = Column(Integer)
    angle = Column(Integer)
    __table_args__ = (UniqueConstraint("make", "length", "angle", name="unique_stem"),)



# Define the Frames table
class Frame(Base):
    __tablename__ = "frames"
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    size = Column(String, index=True)
    reach = Column(Float)
    stack = Column(Float)
    top_tube = Column(Float)
    head_angle = Column(Float)
    seat_angle = Column(Float)
    head_tube = Column(Float)
    chainstay = Column(Float)
    wheelbase = Column(Float)
    front_centre = Column(Float, nullable=True)
    bb_drop = Column(Float, nullable=True)
    fork_rake = Column(Float, nullable=True)
    __table_args__ = (UniqueConstraint("make", "size", "reach", "stack", "top_tube", name="unique_frame"),)



#definte the handlebars table
class Handlebar(Base):
    __tablename__ = "handlebars"
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    width = Column(Integer)
    reach = Column(Integer)
    drop = Column(Integer)
    __table_args__ = (UniqueConstraint("make", "width", "reach", "drop", name="unique_handlebar"),)



# Create the table
Base.metadata.create_all(bind=engine)
