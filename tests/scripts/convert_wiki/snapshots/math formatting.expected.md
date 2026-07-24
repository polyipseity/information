## BOTH

Block math with surrounding text on both sides.

Text before the math $$f(x)$$ and text after the math.

## BEFORE\_ONLY

Block math preceded by text only, at line end.

Text before the math only $$g(y)$$

## AFTER\_ONLY

Block math followed by text only, at line start.

$$h(z)$$ and text after the math only.

## NEITHER

Standalone block math on its own line.

$$k(w)$$

## multi-block math

Multiple consecutive block math expressions separated by text.

Start $$a(b)$$ middle $$c(d)$$ end

## INLINE\_MATH

Inline math with surrounding text.

Text $f(x)$ and $g(y)$

## PIPE\_IN\_MATH\_IN\_TABLE

Display math in table cell containing a bare pipe character.

| Column 1                |
| ----------------------- |
| text  $$x\vert y$$ more |

## ESCAPED\_PIPE\_IN\_MATH

Escaped pipe in display math \(backslash-pipe preserved\).

Escaped: $$\|x\|$$

## PIPE\_IN\_MATH\_IN\_TABLE\_INLINE

Inline math in table cell containing a bare pipe character.

| Column 1             |
| -------------------- |
| text $x\vert y$ more |
