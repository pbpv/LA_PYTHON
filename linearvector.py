#!/usr/bin/python3

import math


class Vector(object):
    """
    Class Vector object is used to indicate a vector(magnitude and direction)
    The tuple can be used generically as co-ordinates for vector
    """

    tolerance = 1e-10

    def __init__(self, coordinates):
        """
        This function initializes the objects with the coordinates passed in.
        Null coordinates are not allowed and a ValueError is raised.
        If a non-iterable is passed in as coordinates then a type error is
        raised.
        """
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The Coordinates should not be empty")

        except TypeError:
            raise TypeError("The Coordinates should be itterable")

    def __str__(self):
        """This function provides the ability to print the vector and
        limit it to 3 digit precision.
        """
        st = ",".join(format(val, ".3f") for val in self.coordinates)
        st = "(" + st + ")"
        return "Vector {} ".format(st)

    def __eq__(self, v):
        """ This function returns true if the vector object passed in has
        the same co-ordinates as the vector it is compared to
        """
        return self.coordinates == v.coordinates

    def add(self, v):
        """This function returns the sum of 2 vectors if they are of same
        dimensions. The sum is returned as a list"""
        if self.dimension != v.dimension:
            raise TypeError("Please use a vector with the same dimension")

        ret = []

        for index, val in enumerate(self.coordinates):
            ret.append((val + v.coordinates[index]))

        return Vector(ret)

    def sub(self, v):
        """This function returns the subract of 2 vectors if they are of same
        dimensions. The sum is returned as a list"""
        if self.dimension != v.dimension:
            raise TypeError("Please use a vector with the same dimension")

        ret = []

        for index, val in enumerate(self.coordinates):
            ret.append((val - v.coordinates[index]))

        return Vector(ret)

    def scalar_mult(self, v):
        """This function is scalar multiplication of the vector and number.
        The result is returned as a list"""

        ret = []

        for val in self.coordinates:
            ret.append((val * v))

        return Vector(ret)

    def magnitude(self):
        """This function calculates magnitude of vector"""

        newlist = [math.pow(x, 2) for x in self.coordinates]

        return math.sqrt(sum(newlist))

    def normalization(self):
        """This function returns the unit vector normalization
        """
        try:
            return self.scalar_mult(1/(self.magnitude()))
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot normalize a vector of 0 magnitude")

    def dotproduct(self, v):
        """This function calculates the dot product of 2 vectors"""

        if self.dimension != v.dimension:
            raise TypeError("Please use a vector with the same dimension")

        new_list = [x*y for x, y in zip(self.coordinates, v.coordinates)]

        return sum(new_list)

    def angle_between_vectors(self, v):
        """This function provides the angle between vectors in radians"""

        try:
            return math.acos(self.dotproduct(v) / (self.magnitude() *
                                                v.magnitude()))

        except ZeroDivisionError:
            raise ZeroDivisionError("None of the magnitudes can be zero")

    def is_orthogonal(self, v):
        """This function returns true if v is orthogonal to self"""
        return abs(self.dotproduct(v)) < self.tolerance

    def is_parallel(self, v):
        """This function returns true if v is paralled to self"""

        return (self.magnitude() < self.tolerance or v.magnitude() < self.tolerance
        or self.angle_between_vectors(v) == 0 or
        self.angle_between_vectors(v) == math.pi)

    def projection(self, v):
        """This function returns projection of V on self"""

        a = (self.normalization())
        return a.scalar_mult(v.dotproduct(a))

    def orthogonal_vec(self, v):
        """ The orthogonal vector is vparallel + vorthogonal = v """


        return v.sub((self.projection(v)))

    def cross_product_3d(self, v):
        """ This gives the cross product of 3d vectors """
        if self.dimension != 3 and v.dimension != 3:
            raise TypeError("Both vectors should be 3D vectors")

        (a1, a2, a3) = self.coordinates
        (b1, b2, b3) = v.coordinates
        (c1, c2, c3) = (a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1)


        return Vector((c1, c2, c3))


# Testing the vector initialization.

myvector = Vector([1, 2, 3])
print(myvector)
vector2 = Vector((1, 2, 3))
print(myvector == myvector)

add_vec1 = Vector([8.218, -9.341])
add_vec2 = Vector([-1.129, 2.111])
print("Add vector result = {} ".format(add_vec1.add(add_vec2)))

sub_vec1 = Vector([7.119, 8.215])
sub_vec2 = Vector([-8.223, 0.878])
print("Subtract vector = ", sub_vec1.sub(sub_vec2))

scalar_factor = 7.41
mult_vec1 = Vector([1.671, -1.012, -0.318])
print("Scalar Multiplication = ", mult_vec1.scalar_mult(scalar_factor))

mag_vec1 = Vector([-0.221, 7.437])
print("Magnitude of vector1 = ", mag_vec1.magnitude())

mag_vec2 = Vector([8.813, -1.331, -6.247])
print("Magnitude of vector2 = ", mag_vec2.magnitude())

norm_vec1 = Vector([5.581, -2.136])
norm_vec2 = Vector([1.996, 3.108, -4.554])
print("Normalization of vector1 = ", norm_vec1.normalization())
print("Normalization of vector2 = ", norm_vec2.normalization())

dot_vec_1 = Vector([7.887, 4.138])
dot_vec_2 = Vector([-8.802, 6.776])

print("Dot Product of vec1 and vec2 = ", dot_vec_1.dotproduct(dot_vec_2))

dot_vec_3 = Vector([-5.955, -4.904, -1.874])
dot_vec_4 = Vector([-4.496, -8.755, 7.103])

print("Dot Product of vec3 and vec4 ", dot_vec_3.dotproduct(dot_vec_4))

angle_vec_1 = Vector([3.183, -7.627])
angle_vec_2 = Vector([-2.668, 5.319])

print("Angle between vector 1 and 2 in rad = ",
      angle_vec_1.angle_between_vectors(angle_vec_2))

angle_vec_3 = Vector([7.35, 0.221, 5.188])
angle_vec_4 = Vector([2.751, 8.259, 3.985])

print("Angle betweeb vector 3 and vecto4 in degrees = ",
      math.degrees(angle_vec_3.angle_between_vectors(angle_vec_4)))

par_otho_list1 = Vector([-7.579, -7.88])
par_otho_list2 = Vector([22.737, 23.64])

print("p1 and p2 are Parallel = {} Orthogonal = {}".format(par_otho_list1.
    is_parallel(par_otho_list2), par_otho_list1.is_orthogonal(par_otho_list2)))

par_otho_list3 = Vector([-2.029, 9.97, 4.172])
par_otho_list4 = Vector([-9.231, -6.639, -7.245])

print("p3 and p4 are Parallel = {} Orthogonal = {}".format(par_otho_list3.
    is_parallel(par_otho_list4), par_otho_list3.is_orthogonal(par_otho_list4)))

par_otho_list5 = Vector([-2.328, -7.284, -1.214])
par_otho_list6 = Vector([-1.821, 1.072, -2.94])

print("p5 and p6 are Parallel = {} Orthogonal = {}".format(par_otho_list5.
    is_parallel(par_otho_list6), par_otho_list5.is_orthogonal(par_otho_list6)))


par_otho_list7 = Vector([2.118, 4.827])
par_otho_list8 = Vector([0, 0])

print("p7 and p8 are Parallel = {} Orthogonal = {}".format(par_otho_list7.
    is_parallel(par_otho_list8), par_otho_list7.is_orthogonal(par_otho_list8)))

proj1 = Vector([3.039, 1.879])
proj2 = Vector([0.825, 2.036])

print("Projection of proj1 on prog2 = ", proj2.projection(proj1))

ortho1 = Vector([-9.88, -3.264, -8.159])
ortho2 = Vector([-2.155, -9.353, -9.473])

print("Orthogonal = ", ortho2.orthogonal_vec(ortho1))

finalv1 = Vector([3.009, -6.172, 3.692, -2.51])
finalv2 = Vector([6.404, -9.144, 2.759, 8.718])

print(" Printing Parallel and Orthogonal ", finalv2.projection(finalv1),
      finalv2.orthogonal_vec(finalv1))

cvec1 = Vector([8.462, 7.893, -8.187])
cvec2 = Vector([6.984, -5.975, 4.778])

print("Vector crossprod = ", cvec1.cross_product_3d(cvec2))

cvec3 = Vector([-8.987, -9.838, 5.031])
cvec4 = Vector([-4.268, -1.861, -8.866])
cvectemp = cvec3.cross_product_3d(cvec4)

print("Vector parallelogram area = ", cvectemp.magnitude())

cvec5 = Vector([1.5, 9.547, 3.691])
cvec6 = Vector([-6.007, 0.124, 5.772])

cvectemp1 = cvec5.cross_product_3d(cvec6)
print("Triangle = ", (cvectemp1.magnitude())*0.5)
