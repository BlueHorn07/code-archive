export const OrmConfig: object = {
  type: 'mysql',
  host: 'localhost',
  port: 3306,
  database: 'your_database',
  username: 'your_username',
  password: 'your_password',
  entities: ['dist/**/*.entity.js'],
  synchronize: false, // should be `false` on production environment
};
