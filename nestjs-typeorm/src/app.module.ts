import { Module } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { AppController } from "./app.controller";
import { AppService } from "./app.service";
import { BoardModule } from "./board/board.module";
import { UserModule } from "./user/user.module";
import { ProfileModule } from "./profile/profile.module";
import { OrmConfig } from "./config/ormconfig";

@Module({
  imports: [
    TypeOrmModule.forRoot(OrmConfig),
    BoardModule,
    UserModule,
    ProfileModule,
  ],
  controllers: [AppController],
  providers: [AppService]
})
export class AppModule {}
