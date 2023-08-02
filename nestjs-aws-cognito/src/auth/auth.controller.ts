import { Body, Controller, Post } from '@nestjs/common';
import { AuthService } from './auth.service';
import { LoginRequest, RegisterRequest } from './auth.dto';

@Controller('auth')
export class AuthController {
  constructor(private readonly authService: AuthService) {}

  @Post('register')
  async register(
    @Body() registerRequest: RegisterRequest
  ) {
    console.log(registerRequest);
  }

  @Post('login')
  async login(@Body() loginRequest: LoginRequest) {
    console.log(loginRequest);
  }
}
