import { Body, Controller, Delete, Get, Param, Post, Put } from '@nestjs/common';
import { BookDto, BookSearchDto } from './book.dto';
import { BookService } from './book.service';

@Controller('book')
export class BookController {
  constructor(
    private bookService: BookService
  ) {}

  @Get()
  getAllBook() {
    return this.bookService.getAllBook();
  }

  @Get(':book_id')
  getBookById(@Param('book_id') book_id: string) {
    return this.bookService.getBook(book_id);
  }


  @Post()
  putBook(@Body() dto: BookDto) {
    return this.bookService.putBook(dto);
  }

  @Post('search')
  searchBook(@Body() dto: BookSearchDto) {
    return this.bookService.searchBook(dto);
  }
  

  @Delete(':book_id')
  deleteBookById(@Param('book_id') book_id: string) {
    return this.bookService.deleteBook(book_id);
  }
}
