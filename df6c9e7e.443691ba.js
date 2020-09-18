(window.webpackJsonp=window.webpackJsonp||[]).push([[24],{78:function(e,a,t){"use strict";t.r(a),t.d(a,"frontMatter",(function(){return c})),t.d(a,"metadata",(function(){return r})),t.d(a,"rightToc",(function(){return m})),t.d(a,"default",(function(){return i}));var n=t(2),s=t(6),p=(t(0),t(86)),c={id:"sum",title:"sum",sidebar_label:"sum"},r={unversionedId:"api/sum",id:"api/sum",isDocsHomePage:!1,title:"sum",description:"`python",source:"@site/docs/api/sum.md",permalink:"/vecpy/docs/api/sum",editUrl:"https://github.com/ooreilly/vecpy/docs/api/sum.md",sidebar_label:"sum",sidebar:"API",previous:{title:"elementwise",permalink:"/vecpy/docs/api/elementwise"},next:{title:"to_numpy",permalink:"/vecpy/docs/api/to_numpy"}},m=[{value:"Args",id:"args",children:[]},{value:"Returns",id:"returns",children:[]},{value:"Example",id:"example",children:[]}],b={rightToc:m};function i(e){var a=e.components,t=Object(s.a)(e,["components"]);return Object(p.b)("wrapper",Object(n.a)({},b,t,{components:a,mdxType:"MDXLayout"}),Object(p.b)("pre",null,Object(p.b)("code",Object(n.a)({parentName:"pre"},{className:"language-python"}),"def sum(expr: vecpy.base.Expr, deviceID=0) -> float:\n")),Object(p.b)("hr",null),Object(p.b)("p",null,"Return the sum of each value in a vector expression."),Object(p.b)("h2",{id:"args"},"Args"),Object(p.b)("ul",null,Object(p.b)("li",{parentName:"ul"},Object(p.b)("strong",{parentName:"li"},"expr"),"  : VecPy expression to sum."),Object(p.b)("li",{parentName:"ul"},Object(p.b)("strong",{parentName:"li"},"deviceID")," (optional) : device ID to use.")),Object(p.b)("h2",{id:"returns"},"Returns"),Object(p.b)("p",null,"The sum of the expression."),Object(p.b)("h2",{id:"example"},"Example"),Object(p.b)("p",null,"Compute the l2-norm, ",Object(p.b)("span",Object(n.a)({parentName:"p"},{className:"math math-inline"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"katex"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"katex-mathml"}),Object(p.b)("math",Object(n.a)({parentName:"span"},{xmlns:"http://www.w3.org/1998/Math/MathML"}),Object(p.b)("semantics",{parentName:"math"},Object(p.b)("mrow",{parentName:"semantics"},Object(p.b)("mi",Object(n.a)({parentName:"mrow"},{mathvariant:"normal"}),"\u2225"),Object(p.b)("mi",{parentName:"mrow"},"x"),Object(p.b)("mi",Object(n.a)({parentName:"mrow"},{mathvariant:"normal"}),"\u2225"),Object(p.b)("mo",{parentName:"mrow"},"="),Object(p.b)("msqrt",{parentName:"mrow"},Object(p.b)("mrow",{parentName:"msqrt"},Object(p.b)("msub",{parentName:"mrow"},Object(p.b)("mo",{parentName:"msub"},"\u2211"),Object(p.b)("mi",{parentName:"msub"},"i")),Object(p.b)("msubsup",{parentName:"mrow"},Object(p.b)("mi",{parentName:"msubsup"},"x"),Object(p.b)("mi",{parentName:"msubsup"},"i"),Object(p.b)("mn",{parentName:"msubsup"},"2"))))),Object(p.b)("annotation",Object(n.a)({parentName:"semantics"},{encoding:"application/x-tex"}),"\\|x\\| = \\sqrt{\\sum_i x_i^2}")))),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"katex-html","aria-hidden":"true"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"base"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"strut",style:{height:"1em",verticalAlign:"-0.25em"}})),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mord"}),"\u2225"),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mord mathnormal"}),"x"),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mord"}),"\u2225"),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mspace",style:{marginRight:"0.2777777777777778em"}})),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mrel"}),"="),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mspace",style:{marginRight:"0.2777777777777778em"}}))),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"base"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"strut",style:{height:"1.24em",verticalAlign:"-0.3069010000000002em"}})),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mord sqrt"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-t vlist-t2"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-r"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist",style:{height:"0.9330989999999998em"}}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"svg-align",style:{top:"-3.2em"}}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"pstrut",style:{height:"3.2em"}})),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mord",style:{paddingLeft:"1em"}}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mop"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mop op-symbol small-op",style:{position:"relative",top:"-0.0000050000000000050004em"}}),"\u2211"),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"msupsub"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-t vlist-t2"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-r"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist",style:{height:"0.16195399999999993em"}}),Object(p.b)("span",Object(n.a)({parentName:"span"},{style:{top:"-2.40029em",marginLeft:"0em",marginRight:"0.05em"}}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"pstrut",style:{height:"2.7em"}})),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"sizing reset-size6 size3 mtight"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mord mathnormal mtight"}),"i")))),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-s"}),"\u200b")),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-r"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist",style:{height:"0.29971000000000003em"}}),Object(p.b)("span",{parentName:"span"})))))),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mspace",style:{marginRight:"0.16666666666666666em"}})),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mord"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mord mathnormal"}),"x"),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"msupsub"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-t vlist-t2"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-r"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist",style:{height:"0.7959080000000001em"}}),Object(p.b)("span",Object(n.a)({parentName:"span"},{style:{top:"-2.4231360000000004em",marginLeft:"0em",marginRight:"0.05em"}}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"pstrut",style:{height:"2.7em"}})),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"sizing reset-size6 size3 mtight"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mord mathnormal mtight"}),"i"))),Object(p.b)("span",Object(n.a)({parentName:"span"},{style:{top:"-3.0448000000000004em",marginRight:"0.05em"}}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"pstrut",style:{height:"2.7em"}})),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"sizing reset-size6 size3 mtight"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"mord mtight"}),"2")))),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-s"}),"\u200b")),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-r"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist",style:{height:"0.27686399999999994em"}}),Object(p.b)("span",{parentName:"span"})))))))),Object(p.b)("span",Object(n.a)({parentName:"span"},{style:{top:"-2.893099em"}}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"pstrut",style:{height:"3.2em"}})),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"hide-tail",style:{minWidth:"1.02em",height:"1.28em"}}),Object(p.b)("svg",Object(n.a)({parentName:"span"},{width:"400em",height:"1.28em",viewBox:"0 0 400000 1296",preserveAspectRatio:"xMinYMin slice"}),Object(p.b)("path",Object(n.a)({parentName:"svg"},{d:"M263,681c0.7,0,18,39.7,52,119\nc34,79.3,68.167,158.7,102.5,238c34.3,79.3,51.8,119.3,52.5,120\nc340,-704.7,510.7,-1060.3,512,-1067\nl0 -0\nc4.7,-7.3,11,-11,19,-11\nH40000v40H1012.3\ns-271.3,567,-271.3,567c-38.7,80.7,-84,175,-136,283c-52,108,-89.167,185.3,-111.5,232\nc-22.3,46.7,-33.8,70.3,-34.5,71c-4.7,4.7,-12.3,7,-23,7s-12,-1,-12,-1\ns-109,-253,-109,-253c-72.7,-168,-109.3,-252,-110,-252c-10.7,8,-22,16.7,-34,26\nc-22,17.3,-33.3,26,-34,26s-26,-26,-26,-26s76,-59,76,-59s76,-60,76,-60z\nM1001 80h400000v40h-400000z"})))))),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-s"}),"\u200b")),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist-r"}),Object(p.b)("span",Object(n.a)({parentName:"span"},{className:"vlist",style:{height:"0.3069010000000002em"}}),Object(p.b)("span",{parentName:"span"})))))))))),Object(p.b)("pre",null,Object(p.b)("code",Object(n.a)({parentName:"pre"},{className:"language-python"})," \n>>> import numpy as np\n>>> x = np.ones(10)\n>>> # Copy to GPU\n>>> vx = vecpy.to_vecpy(x)\n>>> # Compute l2 norm\n>>> norm = vecpy.sum(vecpy.sqrt(vx ** 2))\n>>> norm.get()\narray([10.])\n \n")))}i.isMDXComponent=!0},86:function(e,a,t){"use strict";t.d(a,"a",(function(){return l})),t.d(a,"b",(function(){return j}));var n=t(0),s=t.n(n);function p(e,a,t){return a in e?Object.defineProperty(e,a,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[a]=t,e}function c(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,n)}return t}function r(e){for(var a=1;a<arguments.length;a++){var t=null!=arguments[a]?arguments[a]:{};a%2?c(Object(t),!0).forEach((function(a){p(e,a,t[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):c(Object(t)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(t,a))}))}return e}function m(e,a){if(null==e)return{};var t,n,s=function(e,a){if(null==e)return{};var t,n,s={},p=Object.keys(e);for(n=0;n<p.length;n++)t=p[n],a.indexOf(t)>=0||(s[t]=e[t]);return s}(e,a);if(Object.getOwnPropertySymbols){var p=Object.getOwnPropertySymbols(e);for(n=0;n<p.length;n++)t=p[n],a.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(s[t]=e[t])}return s}var b=s.a.createContext({}),i=function(e){var a=s.a.useContext(b),t=a;return e&&(t="function"==typeof e?e(a):r(r({},a),e)),t},l=function(e){var a=i(e.components);return s.a.createElement(b.Provider,{value:a},e.children)},O={inlineCode:"code",wrapper:function(e){var a=e.children;return s.a.createElement(s.a.Fragment,{},a)}},o=s.a.forwardRef((function(e,a){var t=e.components,n=e.mdxType,p=e.originalType,c=e.parentName,b=m(e,["components","mdxType","originalType","parentName"]),l=i(t),o=n,j=l["".concat(c,".").concat(o)]||l[o]||O[o]||p;return t?s.a.createElement(j,r(r({ref:a},b),{},{components:t})):s.a.createElement(j,r({ref:a},b))}));function j(e,a){var t=arguments,n=a&&a.mdxType;if("string"==typeof e||n){var p=t.length,c=new Array(p);c[0]=o;var r={};for(var m in a)hasOwnProperty.call(a,m)&&(r[m]=a[m]);r.originalType=e,r.mdxType="string"==typeof e?e:n,c[1]=r;for(var b=2;b<p;b++)c[b]=t[b];return s.a.createElement.apply(null,c)}return s.a.createElement.apply(null,t)}o.displayName="MDXCreateElement"}}]);