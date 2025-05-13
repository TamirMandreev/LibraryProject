import pytest
from library.models import Author, Book, Review


@pytest.fixture
def author():
    """Создание экземпляра модели Author"""
    author = Author.objects.create(
        first_name="Tamir", last_name="Mandreev", birth_date="1997-12-27"
    )
    return author


@pytest.fixture
def book(author):
    """Создание экземпляра модели Book"""
    book = Book.objects.create(
        title="Атлант расправил плечи",
        publication_date="1997-12-27",
        author=author,
        review="Хорошая книга",
        recommend="Советую читать медленно и вдумчиво",
    )
    return book


@pytest.fixture
def review(book):
    review = Review.objects.create(book=book, rating=10, comment="Комментарий")
    return review


# Тестирование модели Author
@pytest.mark.django_db
def test_create_author(author):
    """Тест создания объекта модели Author"""

    assert author.first_name == "Tamir"
    assert author.last_name == "Mandreev"
    assert author.birth_date == "1997-12-27"


@pytest.mark.django_db
def test_str_method_author(author):
    """Тест метода __str__ модели Author"""
    assert author.__str__() == "Tamir Mandreev"


# Тестирование модели Book
@pytest.mark.django_db
def test_create_book(author, book):
    """Тест создания объекта модели Book"""
    assert book.title == "Атлант расправил плечи"
    assert book.publication_date == "1997-12-27"
    assert book.author == author
    assert book.review == "Хорошая книга"
    assert book.recommend == "Советую читать медленно и вдумчиво"


@pytest.mark.django_db
def test_str_method_book(book):
    """Тест метода __str__ модели Book"""
    assert book.__str__() == "Атлант расправил плечи"


# Тестирование модели Review
@pytest.mark.django_db
def test_create_review(review, book):
    """Тест создания объекта модели Review"""
    assert review.book == book
    assert review.rating == 10
    assert review.comment == "Комментарий"


@pytest.mark.django_db
def test_str_method_review(review, book):
    assert review.__str__() == f"Review for {book.title}"
