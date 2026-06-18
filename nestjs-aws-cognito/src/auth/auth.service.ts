import { Injectable } from '@nestjs/common';
import {
  CognitoIdentityProviderClient,
  AdminCreateUserCommand,
} from '@aws-sdk/client-cognito-identity-provider';

@Injectable()
export class AuthService {
  private readonly cognitoClient = new CognitoIdentityProviderClient({
    region: 'ap-northeast-2',
  });
  private readonly USER_POOL_ID = 'ap-northeast-2_RXNM6G6EG';

  async register() {
    const input = {
      UserPoolId: this.USER_POOL_ID,
      Username: 'seokyun_test',
    };

    const command = new AdminCreateUserCommand(input);
    const res = await this.cognitoClient.send(command);
    console.log(res);
  }
}
