import { Injectable } from '@nestjs/common';
import {
  DeleteItemCommand,
  DynamoDBClient,
  GetItemCommand,
  PutItemCommand,
  ScanCommand,
} from '@aws-sdk/client-dynamodb';

/**
 * The Book Repository only using `@aws-sdk/client-dynamodb`.
 * Please, see and compare the code of `book.lib.repository.ts` also.
 */

@Injectable()
export class BookClientRepository {
  private tableName: string;
  private dynamodb: DynamoDBClient;

  constructor() {
    this.tableName = 'online-library';
    this.dynamodb = new DynamoDBClient({ region: 'ap-northeast-2' });
  }

  /**
   * Query
   */

  async getBook(book_id: string) {
    const getCommand = new GetItemCommand({
      TableName: this.tableName,
      Key: {
        book_id: { S: book_id },
      },
    });

    const res = await this.dynamodb.send(getCommand);
    return res['Item'];
  }


  /**
   * Scan
   */

  async getAllBook() {
    const scanCommand = new ScanCommand({
      TableName: this.tableName,
    });

    const res = await this.dynamodb.send(scanCommand);
    return res['Items'];
  }

  async searchBookByContent(content_keyword: string) {
    const scanCommand = new ScanCommand({
      TableName: this.tableName,
      FilterExpression: `contains (content, :keyword)`,
      ExpressionAttributeValues: {
        ':keyword': {S: content_keyword}
      },
    })

    const res = await this.dynamodb.send(scanCommand);
    return res['Items'];
  }


  /**
   * Put
   */

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

    return this.dynamodb.send(putCommand);
  }


  /**
   * Delete
   */

  deleteBook(book_id: string) {
    const deleteCommand = new DeleteItemCommand({
      TableName: this.tableName,
      Key: {
        book_id: { S: book_id },
      },
    });

    return this.dynamodb.send(deleteCommand);
  }
  
}
