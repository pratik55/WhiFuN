# mars_struct

**Source:** `whifun_functions/private/mars_struct.m:1`

## Signature

```matlab
function varargout = mars_struct(action, varargin)
```

## Summary

Multifunction function for manipulating structures

## Description

To help the exposition a bit: 'fill' in a name, means that values empty or missing in one structure are fetched from another

'merge' means simply that missing fields are added, with values, from a second structure (but not filled if empty)

Each function needs to deal with the case of empty arguments

fills structure fields empty or missing in a from those present in b a, b are structures fieldns (optional) is cell array of field names to fill from in b c is returned structure Is recursive, will fill struct fields from struct fields flags may contain 'f', which Force fills a from b (all non empty fields in b overwrite those in a) flags may also contain 'r', which Restricts fields to write from b, to those that are already present in a

split structure a into two, according to fields in b so that c becomes a structure which contains the fields in a, that are also present in b, and d contains the fields in a that are not present in b.  b can be a structure or a cell array of fieldnames

strips all fields present in b from those in a, returning denuded structure as d. b can be a structure or a cell array of fieldnames.  'strip' is just 'split' but returning only the second argument

merges structure a and b (fields present in b added to a)

force fill, followed by split All fields from a, that are also present in b, and not empty in b, are replaced with the values in b; the result is returned as c Any fields present in a, but not present in b, are returned in d

force fill followed by merge performs 'ffillsplit' on a and b, then merges a and b All fields present in a or b are returned in c, but any fields present in both, now have the value from b

performs 'split' on a and b, creating c and d then merges c with b. d contains fields in a that were not present in b c contains fields present in both, or just in b

returns 1 if field named in b is present in a and field value is not empty. The call is recursive if more than two arguments are passed Thus with structure s = struct('one', struct('two', 3))

returns value of field named in b from a or [] if absent Call is recursive, like 'isthere' above.

returns output like disp(a) as a cell array Useful for printing text description of structure

## Examples

```matlab
c = mars_struct('fillafromb', a, b, fieldns, flags)
[c, d] = mars_struct('split', a, b)
[d] = mars_struct('strip', a, b)
c = mars_struct('merge', a, b)
[c,d] = mars_struct('ffillsplit', a, b)
c = mars_struct('ffillmerge', a, b)
[c d] = mars_struct('splitmerge', a, b)
z = mars_struct('isthere', a, b [, c [, d ...])
mars_struct('isthere', s, 'one', 'two') returns 1
z = mars_struct('getifthere', a, b [, c [, d ...])
strs = mars_struct('celldisp', a)
```
