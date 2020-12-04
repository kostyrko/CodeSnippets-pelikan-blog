Title: Ant Design: Form
Author: mkostyrko
Date: 2020-12-01 10:00
Updated:
Category: react
Tags: react
Slug: react-antd
related_posts: 

![antd-logo](https://miro.medium.com/max/1000/1*fyrm-nSWAyxa5_m78mTq2g.png)

### Tworzenie projektu przy pomocy CRA + instalacja ANTD

Ant Design jest biblioteką do stylowania komponentów Reactowych (współpracuje również z VUE oraz Angularem (NG-ZORRO)) utrzymywana przez Grupę Alibaba

Stworzenie projektu

    npx create-react-app antd_form

Dodanie zależności -> antd

    npm add antd

Zaimportowanie do App.js odpowiedniego komponentu oraz CSS do App.css

    // App.css - dodanie 1 linijki treści na samej górze
    @import '~antd/dist/antd.css';
    [...]

Zaimportowanie komponentu oraz jego zastosowanie

    //App.js
    import { Button } from 'antd';
    import './App.css';

    function App() {
      return (
        <div>
          <Button type="primary">Button</Button>
        </div>
      );
    }

    export default App;

---
### ANT DESIGN PRO

*ANT DESIGN PRO* jest biblioteką UI należącą do ANT DESIGN reklamującą się jako rozwiązanie dla projektów komercyjnych (przedsiębiorczych/enterprise), ale z dalszego jej opisu możemy się dowiedzieć, że została stworzona pod kątem interfejsów adminowskich.






---

Źródła:


[Ant Design - Form](https://ant.design/components/form/)

[SO - Correctly creating an antd Form using the extends React.Component mechanism](https://stackoverflow.com/questions/41181573/correctly-creating-an-antd-form-using-the-extends-react-component-mechanism)


[Redux Form + antd](https://codesandbox.io/s/jzyl70wpk?file=/index.js)

[Use Form of Ant Design V4 in React Hooks](https://annacoding.com/article/7jDz3vvi3VdtYXYkvYpUp2/Use-Form-of-Ant-Design-V4-in-React-Hooks)

[Chinese Material Design This Chinese Design Language will Make You Want to Switch.](https://uxdesign.cc/chinese-material-design-5d31359df4a6)


YT

[3 - Add Simple Contact Form - Building a Contact Management System With React and Ant Design Library](https://www.youtube.com/watch?v=DaMxXs8Kl90&ab_channel=CodingTheWorld)

