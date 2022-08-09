import { Injectable } from '@nestjs/common';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocument, ScanCommand, GetCommand, PutCommand, DeleteCommand } from "@aws-sdk/lib-dynamodb";

/**
 * The Book Repository using `@aws-sdk/client-dynamodb` and `@aws-sdk/lib-dynamodb`.
 * Please, see and compare the code of `book.client.repository.ts` also.
 */

@Injectable()
export class BookLibRepository {
  private tableName: string;
  private dynamodb: DynamoDBClient;
  private dynamodbDoc: DynamoDBClient;

  constructor() {
    this.tableName = 'online-library';
    this.dynamodb = new DynamoDBClient({ region: 'ap-northeast-2' });
    this.dynamodbDoc = DynamoDBDocument.from(this.dynamodb);
  }

  /**
 * Query
 */

  async getBook(book_id: string) {
    const getCommand = new GetCommand({
      TableName: this.tableName,
      Key: {
        book_id: book_id,
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
        ':keyword': content_keyword
      },
    })

    const res = await this.dynamodb.send(scanCommand);
    return res['Items'];
  }


  /**
   * Put
   */

  putBook(book_id: string, book_name: string, author: string, content: string) {
    const putCommand = new PutCommand({
      TableName: this.tableName,
      Item: {
        book_id: book_id,
        bookbook_name: book_name,
        author: author,
        content: content,
      }
    })

    return this.dynamodb.send(putCommand);
  }


  /**
   * Delete
   */

  deleteBook(book_id: string) {
    const deleteCommand = new DeleteCommand({
      TableName: this.tableName,
      Key: {
        book_id: book_id,
      },
    });

    return this.dynamodb.send(deleteCommand);
  }
  
}
