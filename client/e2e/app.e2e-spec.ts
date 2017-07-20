import { HungTestPage } from './app.po';

describe('hung-test App', () => {
  let page: HungTestPage;

  beforeEach(() => {
    page = new HungTestPage();
  });

  it('should display welcome message', done => {
    page.navigateTo();
    page.getParagraphText()
      .then(msg => expect(msg).toEqual('Welcome to app!!'))
      .then(done, done.fail);
  });
});
