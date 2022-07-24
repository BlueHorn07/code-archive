import { Module } from '@nestjs/common';
import { BookController } from './book.controller';
import { BookRepository } from './book.repository';
import { BookService } from './book.service';

@Module({
  imports: [],
  controllers: [BookController],
  providers: [BookService, BookRepository]
})
export class BookModule {}
