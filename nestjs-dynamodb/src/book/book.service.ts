import { Injectable } from '@nestjs/common';
import { BookDto, BookSearchDto } from './book.dto';
import { BookRepository } from './repository/book.repository';

@Injectable()
export class BookService {
  constructor(
    private bookRepo: BookRepository
  ) {}

  getBook(book_id: string) {
    return this.bookRepo.getBook(book_id);
  }

  getAllBook() {
    return this.bookRepo.getAllBook();
  }

  searchBook(searchDto: BookSearchDto) {
    const {content} = searchDto;
    return this.bookRepo.searchBookByContent(content);
  }

  putBook(bookDto: BookDto) {
    const {book_id, book_name, author, content} = bookDto;
    return this.bookRepo.putBook(book_id, book_name, author, content);
  }

  deleteBook(book_id: string) {
    return this.bookRepo.deleteBook(book_id);
  }

}
