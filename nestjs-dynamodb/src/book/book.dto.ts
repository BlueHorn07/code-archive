export class BookDto {
  readonly book_id: string;
  readonly book_name: string;
  readonly author: string;
  readonly content: string;
}

export class BookSearchDto {
  readonly content: string;
}
