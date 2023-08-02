import { Body, Controller, Post } from '@nestjs/common';
import { AuthService } from './auth.service';

@Controller('auth')
export class AuthController {
  constructor(private readonly authService: AuthService) {}

  @Post('register')
  async register(
    @Body() registerRequest: { name: string; password: string; email: string },
  ) {
    console.log(registerRequest);
  }

  @Post('login')
  async login(@Body() loginRequest: { name: string; password: string }) {
    console.log(loginRequest);
  }
}
