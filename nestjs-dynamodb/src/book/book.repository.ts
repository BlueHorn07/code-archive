import { Injectable } from '@nestjs/common';
import {
  DeleteItemCommand,
  DynamoDBClient,
  GetItemCommand,
  PutItemCommand,
  ScanCommand,
} from '@aws-sdk/client-dynamodb';

@Injectable()
export class BookRepository {
  private tableName: string;
  private dynmodb: DynamoDBClient;

  constructor() {
    this.tableName = 'online-library';
    this.dynmodb = new DynamoDBClient({ region: 'ap-northeast-2' });
  }

  getAllBook() {
    const scanCommand = new ScanCommand({
      TableName: this.tableName,
    });

    return this.dynmodb.send(scanCommand);
  }

  getBook(book_id: string) {
    const getCommand = new GetItemCommand({
      TableName: this.tableName,
      Key: {
        book_id: { S: book_id },
      },
    });

    return this.dynmodb.send(getCommand);
  }

  searchBookByContent(content_keyword: string) {
    const scanCommand = new ScanCommand({
      TableName: this.tableName,
      FilterExpression: `contains (content, :keyword)`,
      ExpressionAttributeValues: {
        ':keyword': {S: content_keyword}
      },
    })

    return this.dynmodb.send(scanCommand);
  }

  putBook(book_id: string, book_name: string, author: string, content: string) {
    const putCommand = new PutItemCommand({
      TableName: this.tableName,
      Item: {
        book_id: {S: book_id},
        bookbook_name: {S: book_name},
        author: {S: author},
        content: {S: content},
      }
    })

    return this.dynmodb.send(putCommand);
  }

  deleteBook(book_id: string) {
    const deleteCommand = new DeleteItemCommand({
      TableName: this.tableName,
      Key: {
        book_id: { S: book_id },
      },
    });

    return this.dynmodb.send(deleteCommand);
  }

  updateBook(book_id: string, ) {

  }
}
