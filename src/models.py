from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey 
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    posts: Mapped[list["Post"]] = relationship(back_populates = "author")

    Followers: Mapped[list["User"]] = relationship(back_populates = "user_from_id")
    Followers: Mapped[list["User"]] = relationship(back_populates = "user_to_id")


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Post (db.Model): 

    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    text:  Mapped[str] = mapped_column(String(200), nullable=False)

    id_user: Mapped[int] = mapped_column(ForeignKey("user.id"))

    coments: Mapped[list["Comments"]] = relationship(back_populates = "posts")
    media: Mapped[list["Media"]] = relationship(back_populates = "posts")
    author: Mapped["User"] = relationship(back_populates = "posts")
   
    

class Comments (db.Model): 

    __tablename__ = "coments"

    id: Mapped[int] = mapped_column(primary_key=True)
    comments_text:  Mapped[str] = mapped_column(String(100), nullable=False)

    id_user: Mapped[int] = mapped_column(ForeignKey("user.id"))
    id_post: Mapped[int] = mapped_column(ForeignKey("post.id"))

    author: Mapped["User"] = relationship(back_populates = "posts")
   

class Media (db.Model): 

    __tablename__ = "media"

    id: Mapped[int] = mapped_column(primary_key=True)

    type: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)

    id_post: Mapped[int] = mapped_column(ForeignKey("post.id"))


class Followers (db.Model): 

    __tablename__ = "followers"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    