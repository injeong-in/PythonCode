var data = {
  "version": "4.5.6",
  "flags": {},
  "shapes": [
    {
      "label": "OilTanker",
      "points": [
        [
          1903.0,
          987.5
        ],
        [
          1477.5,
          987.0
        ],
        [
          1475.5,
          883.0
        ],
        [
          1480.0,
          874.5
        ],
        [
          1539.0,
          852.5
        ],
        [
          1603.0,
          838.5
        ],
        [
          1635.0,
          836.5
        ],
        [
          1660.0,
          830.5
        ],
        [
          1728.0,
          831.5
        ],
        [
          1745.0,
          829.5
        ],
        [
          1750.5,
          825.0
        ],
        [
          1753.5,
          811.0
        ],
        [
          1761.5,
          805.0
        ],
        [
          1765.5,
          796.0
        ],
        [
          1766.5,
          763.0
        ],
        [
          1776.5,
          729.0
        ],
        [
          1778.5,
          688.0
        ],
        [
          1774.0,
          679.5
        ],
        [
          1754.0,
          665.5
        ],
        [
          1743.5,
          654.0
        ],
        [
          1743.5,
          647.0
        ],
        [
          1760.5,
          629.0
        ],
        [
          1765.5,
          617.0
        ],
        [
          1777.5,
          606.0
        ],
        [
          1780.5,
          599.0
        ],
        [
          1780.5,
          531.0
        ],
        [
          1783.5,
          503.0
        ],
        [
          1793.5,
          489.0
        ],
        [
          1793.5,
          468.0
        ],
        [
          1799.0,
          458.5
        ],
        [
          1805.5,
          462.0
        ],
        [
          1805.5,
          483.0
        ],
        [
          1813.0,
          488.5
        ],
        [
          1837.5,
          497.0
        ],
        [
          1824.5,
          511.0
        ],
        [
          1823.5,
          516.0
        ],
        [
          1826.5,
          526.0
        ],
        [
          1823.5,
          544.0
        ],
        [
          1826.5,
          560.0
        ],
        [
          1824.5,
          597.0
        ],
        [
          1839.0,
          613.5
        ],
        [
          1848.5,
          619.0
        ],
        [
          1853.5,
          638.0
        ],
        [
          1863.5,
          654.0
        ],
        [
          1863.5,
          662.0
        ],
        [
          1840.0,
          675.5
        ],
        [
          1834.5,
          683.0
        ],
        [
          1836.5,
          753.0
        ],
        [
          1846.5,
          768.0
        ],
        [
          1851.5,
          797.0
        ],
        [
          1864.5,
          805.0
        ],
        [
          1867.5,
          826.0
        ],
        [
          1882.0,
          834.5
        ],
        [
          1903.5,
          832.0
        ]
      ],
      "group_id": null,
      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "OilTanker",
      "points": [
        [
          858.68511119364,
          521.0091901785931
        ],
        [
          850.7082325809232,
          514.4195948028707
        ],
        [
          854.407654546241,
          503.0901150340846
        ],
        [
          865.2747065693624,
          500.8935832421771
        ],
        [
          877.9220207195668,
          488.0773051079799
        ],
        [
          904.6619474594935,
          488.4436054742803
        ],
        [
          909.4238522213983,
          507.8575248881997
        ],
        [
          911.2553540529001,
          521.0443380750129
        ]
      ],
      "group_id": null,
      "shape_type": "polygon",
      "flags": {}
    }
  ]
}

// var vectorData = JSON.stringify(data.shapes[0].points)
// var vectorData2 = JSON.stringify(data.shapes[1].points)

// console.log(JSON.stringify(data.shapes))

if(data.shapes.length > 2) {
  console.log(data.imagePath +'는 비정상입니다');
} else {
  console.log('통과');
}

console.log(data.shapes.length); //클래스 갯수 구하기
console.log(JSON.stringify(data.shapes));



// var def = function (integer,count,sum_value) {
//   if(integer >= count) 
//     return;
//   integer += 1;
//   sum_value += integer;
//   console.log(sum_value);
//   def(integer, count, sum_value);
// }

// def(0,10,0);
